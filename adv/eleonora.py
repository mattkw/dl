import adv_test
import adv

def module():
    return Eleonora

class Eleonora(adv.Adv):
    a3 = ('prep','50%')

    def init(this):
        this.dmg_make("o_s1_poison",2.65)
        this.dmg_make("o_s1_poison",2.65)
        this.dmg_make("o_s1_poison",2.65)

        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """



if __name__ == '__main__':
    module().comment = 'poison by s1 3 times'
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5 
        """
    adv_test.test(module(), conf, verbose=0)
