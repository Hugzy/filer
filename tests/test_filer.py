
from pytest import raises
from filer.main import FilerTest

def test_filer():
    # test filer without any subcommands or arguments
    with FilerTest() as app:
        app.run()
        assert app.exit_code == 0


def test_filer_debug():
    # test that debug mode is functional
    argv = ['--debug']
    with FilerTest(argv=argv) as app:
        app.run()
        assert app.debug is True


def test_command1():
    # test command1 without arguments
    argv = ['command1']
    with FilerTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'bar'
        assert output.find('Foo => bar')


    # test command1 with arguments
    argv = ['command1', '--foo', 'not-bar']
    with FilerTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'not-bar'
        assert output.find('Foo => not-bar')
