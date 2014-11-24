__author__ = 'elijahfoster-wysocki'

#codecademy lesson

pyg = 'ay'

original = raw_input('Enter a word: ')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:] + first + pyg

    print "Original: " + original
    print "Pig Latin: " + new_word
else:
    print 'empty'