import pytest

from toolkit.__main__ import main


def test_cli_convert(capsys):
    main(['convert','1000','--from','mm','--to','m'])
    captured = capsys.readouterr()
    assert captured.out.strip() == '1'


def test_cli_error_2(capsys):
    with pytest.raises(SystemExit) as exit_info:
        main(['calc','2*/3'])
    assert exit_info.value.code == 2
    captured = capsys.readouterr()
    assert captured.out == ''
    assert 'Ошибка' in captured.err


def test_cli_help(capsys):
    with pytest.raises(SystemExit) as exit_info:
        main(['--help'])
    assert exit_info.value.code == 0