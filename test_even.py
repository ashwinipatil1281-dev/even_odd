from even import even_odd

def test_prime_and_even():
    result = even_odd(7)
    assert result == ("Prime", "Odd")