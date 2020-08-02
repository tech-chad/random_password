from unittest import mock

import pytest

import randpass


@mock.patch.object(randpass, "SPECIAL", ["@"])
def test_generate_password_default():
    result = randpass.generate_password(["a", "B", "1"], 10, 0)
    assert len(result) == 10
    assert "1" in result
    assert "B" in result
    assert "a" in result
    assert "@" not in result


@pytest.mark.parametrize("test_length", [6, 8, 15, 20, 50])
def test_generate_password_length_no_special(test_length):
    result = randpass.generate_password(["a", "B", "1"], test_length, 0)
    assert len(result) == test_length


@pytest.mark.parametrize("test_length", [6, 8, 15, 20, 50])
@mock.patch.object(randpass, "SPECIAL", ["@"])
def test_generate_password_length_one_special(test_length):
    result = randpass.generate_password(["a", "B", "1"], test_length, 1)
    assert len(result) == test_length
    assert "@" in result


@pytest.mark.parametrize("num_special", [1, 2, 5])
@mock.patch.object(randpass, "SPECIAL", ["@"])
def test_generate_password_special(num_special):
    result = randpass.generate_password(["a", "B", "1"], 10, num_special)
    assert len(result) == 10
    assert "@" in result
    assert result.count("@") == num_special


@mock.patch.object(randpass, "UPPER_LETTERS", ("A", "B", "C"))
@mock.patch.object(randpass, "LOWER_LETTERS", ("a", "b", "c"))
@mock.patch.object(randpass, "DIGITS", ("1", "2", "3"))
def test_make_possible():
    result = randpass.make_possible()
    assert result == ["A", "B", "C", "a", "b", "c", "1", "2", "3"]


# argument parsing
@pytest.mark.parametrize("test_value, expected_result", [
    ([], 10), (["-l", "8"], 8), (["-l", "20"], 20)
])
def test_argument_parsing_length(test_value, expected_result):
    result = randpass.argument_parsing(test_value)
    assert result.length == expected_result


@pytest.mark.parametrize("test_value, expected_result", [
    ([], 0), (["-s", "1"], 1), (["-s", "2"], 2), (["-s", "20"], 20)
])
def test_argument_parsing_special(test_value, expected_result):
    result = randpass.argument_parsing(test_value)
    assert result.special == expected_result


@pytest.mark.parametrize("test_value, expected_result", [
    ([], 1), (["-n", "2"], 2), (["-n", "40"], 40)
])
def test_argument_parsing_number_of_passwords(test_value, expected_result):
    result = randpass.argument_parsing(test_value)
    assert result.number == expected_result


# main testing

@mock.patch.object(randpass, "UPPER_LETTERS", ("A", "B", "C"))
@mock.patch.object(randpass, "LOWER_LETTERS", ("a", "b", "c"))
@mock.patch.object(randpass, "DIGITS", ("1", "2", "3"))
def test_main_default(capsys):
    result = randpass.main([])
    captured = capsys.readouterr().out
    assert result == 0
    assert len(captured.strip()) == 10


@pytest.mark.parametrize("test_args, expected_length", [
    (["-l8"], 8), (["-l", "15"], 15), (["-l", "50"], 50)
])
@mock.patch.object(randpass, "UPPER_LETTERS", ("A", "B", "C"))
@mock.patch.object(randpass, "LOWER_LETTERS", ("a", "b", "c"))
@mock.patch.object(randpass, "DIGITS", ("1", "2", "3"))
def test_main_length(test_args, expected_length, capsys):
    result = randpass.main(test_args)
    captured = capsys.readouterr().out
    assert result == 0
    assert len(captured.strip()) == expected_length


@mock.patch.object(randpass, "UPPER_LETTERS", ("A", "B", "C"))
@mock.patch.object(randpass, "LOWER_LETTERS", ("a", "b", "c"))
@mock.patch.object(randpass, "DIGITS", ("1", "2", "3"))
@mock.patch.object(randpass, "SPECIAL", ["@"])
def test_main_one_special(capsys):
    result = randpass.main(["-s", "1"])
    captured = capsys.readouterr().out
    assert result == 0
    assert len(captured.strip()) == 10
    assert captured.count("@") == 1


@pytest.mark.parametrize("test_parm, expected_len", [
    ([], 1), (["-n", "2"], 2), (["-n", "50"], 50)
])
@mock.patch.object(randpass, "UPPER_LETTERS", ("A", "B", "C"))
@mock.patch.object(randpass, "LOWER_LETTERS", ("a", "b", "c"))
@mock.patch.object(randpass, "DIGITS", ("1", "2", "3"))
def test_main_number_of_passwords(test_parm, expected_len, capsys):
    result = randpass.main(test_parm)
    captured = capsys.readouterr().out
    assert result == 0
    captured = captured.splitlines()
    assert len(captured) == expected_len
