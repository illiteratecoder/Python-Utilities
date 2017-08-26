def fake_load(t):
    """Prints a fake progress bar that take t seconds to complete loading."""
    
    from time import sleep

    for i in range(1, 101):
        print("\r{:>6}% |{:<30}|".format(i, u"\u2588" * round(i // 3.333)), end='', flush=True)
        sleep(t/100)

    sleep(0.1)
    print("\n")