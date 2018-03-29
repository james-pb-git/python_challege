import sys
import string
import utils
import re

class ChallengeSolution(object):

    def level0(self):
        print 2**38

    def level1(self):
        input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. \
        bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle \
        qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

        char_map = dict()
        # ATTENTION: use ord()!
        for (idx, ch) in enumerate(string.lowercase):
            if idx + 2 < len(string.lowercase):
                char_map[ch] = string.lowercase[idx + 2]
            char_map['y'] = 'a'
            char_map['z'] = 'b'
        output = ''.join([char_map[ch] if ch in char_map else ch for ch in input])
        print output
        '''
        Result: i hope you didnt translate it by hand. thats what computers are for.         
        doing it in by hand is inefficient and that's why this text is so long. using         
        string.maketrans() is recommended. now apply on the url.
        '''

        # Soution 2 -- recommended!!
        letters_in = string.lowercase
        letters_out = string.lowercase[2:] + 'ab'
        tran_tab = string.maketrans(letters_in, letters_out)
        print input.translate(tran_tab)
        print 'map'.translate(tran_tab)

    def level2(self):
        mess = utils.mess_level2
        print ''.join([ch if ch in string.lowercase else '' for ch in mess])

    def level3_sol1(self):
        mess = utils.mess_level3
        mess = 'a' + mess + 'a'  # Add two lowercase letters to reduce the complexity of edge cases.
        mess = mess.replace('\n', '')
        res = ''
        for (idx, ch) in enumerate(mess):
            if idx + 8 >= len(mess):
                break
            if mess[idx].islower() and mess[idx+4].islower() and mess[idx+8].islower()\
                    and mess[idx+1].isupper() and mess[idx+2].isupper() and mess[idx+3].isupper() \
                    and mess[idx+5].isupper() and mess[idx+6].isupper() and mess[idx+7].isupper():
                res += mess[idx+4]
        print res

    def level3_sol2(self):
        mess = utils.mess_level3
        mess = 'a' + mess + 'a'
        mess = mess.replace('\n', '')
        classification = ''.join(['1' if ch.isupper() else '0' for ch in mess])
        print ''.join([mess[idx.start()+4] for idx in re.finditer('011101110', classification)])


if __name__ == '__main__':
    challenge_solution = ChallengeSolution()
    challenge_solution.level3()