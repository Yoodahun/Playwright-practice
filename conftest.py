import os
from typing import Dict

import pytest
from slugify import slugify


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: Dict, is_webkit, is_chromium, is_firefox):
    args = {**browser_type_launch_args}

    if is_firefox:
        args["firefox_user_prefs"] = {
            "permissions.default.microphone": 1,
            "permissions.default.camera": 1

        }

    return args


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args: Dict, is_chromium: bool):
    args = {
        **browser_context_args
    }

    if is_chromium:
        args["permissions"] = ["camera", "microphone"]

    return args

@pytest.fixture
def build_trace_viewer_file_dir(pytestconfig, request) -> str:
    return os.path.join(pytestconfig.getoption("--output"), slugify(request.node.nodeid))
