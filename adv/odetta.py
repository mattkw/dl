import adv_test
from adv import *

def module():
    return Odetta

class Odetta(Adv):
    a1 = ('a',0.1,'hp70')
    a3 = ('bt',0.2)
    
    def pre(this):
        if this.condition('buff all team'):
            this.s2_proc = this.c_s2_proc
    
    def c_s2_proc(this, e):
        Teambuff('s2',0.15,15).on()

    def s2_proc(this, e):
        Selfbuff('s2',0.15,15).on()



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1,fsc
        `s2,fsc
        `s3,fsc
        `fs, seq=3
        """
    adv_test.test(module(), conf, verbose=-2)


