from hello import main

def test_hello_prints_correct_string(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"
