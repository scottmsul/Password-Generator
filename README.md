# Password Generator

This Python script generates a random memorable password by selecting words from a dictionary.
The list of words is taken from this [blog post](http://preshing.com/20110811/xkcd-password-generator/), with the actual list in this [PHP script](http://preshing.com/files/xkcd_pw.js.php).
When generating words, the script uses `random.SystemRandom`, which relies on `/dev/urandom`.
For why this is important, see [here](http://sockpuppet.org/blog/2014/02/25/safely-generate-random-numbers/).

### Usage

To use, simply type `python password.py` or `python password.py -n 8`.
The script only has one argument, -n (or --num), which is the number of words to generate.
By adding more words, a password will be more difficult to break.
The default is 5 words, while I personally use 8 words for my keepassx password.

### Entropy

The entropy of a password is a measure of how strong it is.
Entropy is related to the number of guesses an attacker would have to attempt in order to brute-force someone's password.
The precise definition of entropy is the log base 2 of the search space.
For example, if a password was a random 5-digit number, the search space would have 10^5 possible passwords, and log2(10^5) = 16.61 bits of entropy.
If a password was on the list of the [1000 most common passwords](http://www.passwordrandom.com/most-popular-passwords) (such as "123456"), it would have at most log2(1000) = 9.97 bits of entropy.

The dictionary contains about 2000 words (1949 to be exact), which is approximately 11 bits of entropy per word.
Some useful information about password entropy can be found on [Wikipedia](https://en.wikipedia.org/wiki/Password_strength#Required_bits_of_entropy).
A strong password might have 50-60 bits, while a physically unbreakable password might have 80-90 bits.
The password generator prints out both the entropy per word and the total entropy.
For more entropy, simply use more words.

### Passwords in general

It is highly recommended that you use a password manager.
This prevents password reuse accross multiple sites, and also leads to very strong passwords for individual websites.
Some good ones are [LastPass](https://lastpass.com/), [KeePass](http://keepass.info/), and [KeePassX](https://www.keepassx.org/).
This script can be good for generating a master password for a password manager, or passwords for which a password manager is not appropriate.
