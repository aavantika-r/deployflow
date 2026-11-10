from app import app


def test_home():
    r = app.test_client().get("/")
    assert r.status_code == 200
    assert b"DeployFlow" in r.data


def test_health():
    assert app.test_client().get("/health").json["status"] == "ok"


def test_version():
    assert app.test_client().get("/version").json["app"] == "deployflow"
