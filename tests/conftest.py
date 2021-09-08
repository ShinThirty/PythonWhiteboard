import json


def pytest_generate_tests(metafunc):
    if "test_case" in metafunc.fixturenames:
        with open("tests/test_whiteboard/test_cases.json", "r") as test_cases_file:
            test_cases = json.load(test_cases_file)
            metafunc.parametrize("test_case", [test_case for test_case in test_cases])
