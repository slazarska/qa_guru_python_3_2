import pytest


@pytest.fixture()
def open_browser():
    assert False, "Check in the fixture"


# fixture == before_all & after_all, pre-, post-conditions

def test_body(open_browser):
    pass
    # перейти на стр логина
    # ввести логин и пароль
    # нажать ОК
    # убедиться, что мы перешли на стр профиля
