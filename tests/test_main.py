
from filer.main import FilerTest

def test_filer(tmp):
    with FilerTest() as app:
        res = app.run()
        print(res)
        raise Exception

def test_command1(tmp):
    argv = ['command1']
    with FilerTest(argv=argv) as app:
        app.run()
