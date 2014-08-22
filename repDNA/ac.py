__author__ = 'liufule12'

from repDNA.util import get_data, generate_phyche_value


class DAC():
    def __init__(self, lag):
        self.lag = lag
        self.k = 2

    def make_dac_vec(self, input_data, phyche_index=None, all_property=False, extra_phyche_index=None):
        if phyche_index is None:
            phyche_index = []
        if extra_phyche_value is None:
            extra_phyche_index = {}

        sequence_list = get_data(input_data)

        phyche_value = generate_phyche_value(self.k, phyche_index, all_property, extra_phyche_index)
        print phyche_value

        from repDNA.acutil import make_ac_vector

        return make_ac_vector(sequence_list, self.lag, phyche_value, self.k)


class DCC():
    def __init__(self, lag):
        self.lag = lag
        self.k = 2

    def make_dcc_vec(self, input_data, phyche_index=None, all_property=False, extra_phyche_index=None):
        if phyche_index is None:
            phyche_index = []
        if extra_phyche_value is None:
            extra_phyche_index = {}

        sequence_list = get_data(input_data)

        phyche_value = generate_phyche_value(self.k, phyche_index, all_property, extra_phyche_index)
        # print phyche_value

        from repDNA.acutil import make_cc_vector

        return make_cc_vector(sequence_list, self.lag, phyche_value, self.k)


class DACC():
    def __init__(self, lag):
        self.lag = lag
        self.k = 2

    def make_dacc_vec(self, input_data, phyche_index=None, all_property=False, extra_phyche_index=None):
        if phyche_index is None:
            phyche_index = []
        if extra_phyche_value is None:
            extra_phyche_index = {}

        sequence_list = get_data(input_data)

        phyche_value = generate_phyche_value(self.k, phyche_index, all_property, extra_phyche_index)
        # print phyche_value

        from repDNA.acutil import make_ac_vector, make_cc_vector

        zipped = zip(make_ac_vector(sequence_list, self.lag, phyche_value, self.k),
                     make_cc_vector(sequence_list, self.lag, phyche_value, self.k))
        vector = [reduce(lambda x, y: x + y, e) for e in zipped]

        return vector


class TAC():
    def __init__(self, lag):
        self.lag = lag
        self.k = 3

    def make_tac_vec(self, input_data, phyche_index=None, all_property=False, extra_phyche_index=None):
        if phyche_index is None:
            phyche_index = []
        if extra_phyche_value is None:
            extra_phyche_index = {}

        sequence_list = get_data(input_data)

        phyche_value = generate_phyche_value(self.k, phyche_index, all_property, extra_phyche_index)
        # print phyche_value

        from repDNA.acutil import make_ac_vector

        return make_ac_vector(sequence_list, self.lag, phyche_value, self.k)


class TCC():
    def __init__(self, lag):
        self.lag = lag
        self.k = 3

    def make_tcc_vec(self, input_data, phyche_index=None, all_property=False, extra_phyche_index=None):
        if phyche_index is None:
            phyche_index = []
        if extra_phyche_value is None:
            extra_phyche_index = {}

        sequence_list = get_data(input_data)

        phyche_value = generate_phyche_value(self.k, phyche_index, all_property, extra_phyche_index)
        # print phyche_value

        from repDNA.acutil import make_cc_vector

        return make_cc_vector(sequence_list, self.lag, phyche_value, self.k)


class TACC():
    def __init__(self, lag):
        self.lag = lag
        self.k = 3

    def make_tacc_vec(self, input_data, phyche_index=None, all_property=False, extra_phyche_index=None):
        if phyche_index is None:
            phyche_index = []
        if extra_phyche_value is None:
            extra_phyche_index = {}

        sequence_list = get_data(input_data)

        phyche_value = generate_phyche_value(self.k, phyche_index, all_property, extra_phyche_index)
        # print phyche_value

        from repDNA.acutil import make_ac_vector, make_cc_vector

        zipped = zip(make_ac_vector(sequence_list, self.lag, phyche_value, self.k),
                     make_cc_vector(sequence_list, self.lag, phyche_value, self.k))
        vector = [reduce(lambda x, y: x + y, e) for e in zipped]

        return vector


if __name__ == '__main__':

    extra_phyche_value = {'AA': [0.06, 0.5, 0.27, 1.59, 0.11, -0.11],
                          'AC': [1.50, 0.50, 0.80, 0.13, 1.29, 1.04],
                          'AG': [0.78, 0.36, 0.09, 0.68, -0.24, -0.62],
                          'AT': [1.07, 0.22, 0.62, -1.02, 2.51, 1.17],
                          'CA': [-1.38, -1.36, -0.27, -0.86, -0.62, -1.25],
                          'CC': [0.06, 1.08, 0.09, 0.56, -0.82, 0.24],
                          'CG': [-1.66, -1.22, -0.44, -0.82, -0.29, -1.39],
                          'CT': [0.78, 0.36, 0.09, 0.68, -0.24, -0.62],
                          'GA': [-0.08, 0.5, 0.27, 0.13, -0.39, 0.71],
                          'GC': [-0.08, 0.22, 1.33, -0.35, 0.65, 1.59],
                          'GG': [0.06, 1.08, 0.09, 0.56, -0.82, 0.24],
                          'GT': [1.50, 0.50, 0.80, 0.13, 1.29, 1.04],
                          'TA': [-1.23, -2.37, -0.44, -2.24, -1.51, -1.39],
                          'TC': [-0.08, 0.5, 0.27, 0.13, -0.39, 0.71],
                          'TG': [-1.38, -1.36, -0.27, -0.86, -0.62, -1.25],
                          'TT': [0.06, 0.5, 0.27, 1.59, 0.11, -0.11]}
    phyche_index = \
        [[0.026, 0.036, 0.031, 0.033, 0.016, 0.026, 0.014, 0.031, 0.025, 0.025, 0.026, 0.036, 0.017, 0.025, 0.016,
          0.026],
         [0.038, 0.038, 0.037, 0.036, 0.025, 0.042, 0.026, 0.037, 0.038, 0.036, 0.042, 0.038, 0.018, 0.038, 0.025,
          0.038]]

    from repDNA.util import normalize_index

    ac = DAC(1)
    vec = ac.make_dac_vec(['GACTGAACTGCACTTTGGTTTCATATTATTTGCTC'], [], all_property=True)
    print(vec)
    print len(vec[0])

    ac = DAC(2)
    vec = ac.make_dac_vec(['GACTGAACTGCACTTTGGTTTCATATTATTTGCTC'], ['Twist', 'Tilt'], all_property=False,
                          extra_phyche_index=normalize_index(phyche_index, is_convert_dict=True))
    print vec
    print len(vec[0])

    cc = DCC(2)
    vec = cc.make_dcc_vec(['GACTGAACTGCACTTTGGTTTCATATTATTTGCTC', 'GACTGAACTGCACTTTGGTTTCATATTATTTGCTC'], [],
                          all_property=True)
    print(vec)
    print len(vec[0]), len(vec[1])

    acc = DACC(1)
    vec = acc.make_dacc_vec(['GACTGAACTGCACTTTGGTTTCATATTATTTGCTC', 'GACTGAACTGCACTTTGGTTTCATATTATTTGCTC'], [],
                            all_property=True)
    for e in vec:
        print e
    print len(vec[0]), len(vec[1])

    acc = DACC(2)
    vec = acc.make_dacc_vec(['GACTGAACTGCACTTTGGTTTCATATTATTTGCTC', 'GACTGAACTGCACTTTGGTTTCATATTATTTGCTC'], [],
                            all_property=True, extra_phyche_index=extra_phyche_value)
    for e in vec:
        print e
    print len(vec[0]), len(vec[1])

    print 'Begin TAC'
    dac = TAC(1)
    vec = dac.make_tac_vec(['GACTGAACTGCACTTTGGTTTCATATTATTTGCTC', 'GACTGAACTGCACTTTGGTTTCATATTATTTGCTC'], [],
                           all_property=True)
    for e in vec:
        print vec
    print len(vec[0]), len(vec[1])

    print 'Begin TCC'
    tcc = TCC(3)
    vec = tcc.make_tcc_vec(['GACTGAACTGCACTTTGGTTTCATATTATTTGCTC', 'GACTGAACTGCACTTTGGTTTCATATTATTTGCTC'], [],
                           all_property=True)
    for e in vec:
        print vec
    print len(vec[0]), len(vec[1])

    print 'Bengin TACC'
    tacc = TACC(3)
    vec = tacc.make_tacc_vec(['GACTGAACTGCACTTTGGTTTCATATTATTTGCTC', 'GACTGAACTGCACTTTGGTTTCATATTATTTGCTC'], [],
                             all_property=True)
    for e in vec:
        print vec
    print len(vec[0]), len(vec[1])