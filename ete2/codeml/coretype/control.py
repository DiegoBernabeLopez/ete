#!/usr/bin/python
#        Author: Francois-Jose Serra
# Creation Date: 2009/08/14 13:56:44

PARAMS = {
    'seqfile'      : 'algn',
    'treefile'     : 'tree',
    'outfile'      : 'out',
    'noisy'        : 0,
    'verbose'      : 2,
    'runmode'      : 0,
    'seqtype'      : 1,
    'CodonFreq'    : 2,
    'clock'        : 0,
    'aaDist'       : 0,
    'model'        : 0,
    'NSsites'      : 2,
    'icode'        : 0,
    'Mgene'        : 0,
    'fix_kappa'    : 0,
    'kappa'        : 2,
    'ndata'        : '*10',
    'fix_omega'    : 0,
    'omega'        : 0.7,
    'fix_alpha'    : 1,
    'alpha'        : 0.,  # if 0 -> infinity
    'Malpha'       : 0,
    'ncatG'        : 8,
    'getSE'        : 0,
    'RateAncestor' : 0,
    'fix_blength'  : 0,
    'Small_Diff'   : '1e-6',
    'cleandata'    : False,
    'method'       : 0
    }

AVAIL = {
    'M0'    :  {'typ': 'null'       , 'evol': 'negative-selection',
                'allow_mark': False,
                'changes': [('NSsites'     , 0),
                            ('alpha'       , '*'),
                            ('method'      , '*'),
                            ('Malpha'      , '*'),
                            ('fix_alpha'   , '*')]},
    'M1'    :  {'typ': 'site'       , 'evol': 'relaxation',
                'allow_mark': False,
                'changes': [('NSsites'     , 1),
                            ('alpha'       , '*'),
                            ('method'      , '*'),
                            ('Malpha'      , '*'),
                            ('fix_alpha'   , '*')]},
    'M2'    :  {'typ': 'site'       , 'evol': 'positive-selection',
                'allow_mark': False,
                'changes': [('NSsites'     , 2),
                            ('omega'       , 1.7),
                            ('alpha'       , '*'),
                            ('method'      , '*'),
                            ('Malpha'      , '*'),
                            ('fix_alpha'   , '*')]},
    'M7'    :  {'typ': 'site'       , 'evol': 'relaxation',
                'allow_mark': False, 
                'changes': [('NSsites'     , 7),
                            ('alpha'       , '*'),
                            ('method'      , '*'),
                            ('Malpha'      , '*'),
                            ('fix_alpha'   , '*')]},
    'M8a'   :  {'typ': 'site'       , 'evol': 'relaxation',
                'allow_mark': False, 
                'changes': [('NSsites'     , 8),
                            ('fix_omega'   , 1),
                            ('omega'       , 1),
                            ('alpha'       , '*'),
                            ('method'      , '*'),
                            ('Malpha'      , '*'),
                            ('fix_alpha'   , '*')]},
    'M8'    :  {'typ': 'site'       , 'evol': 'positive-selection',
                'allow_mark': False, 
                'changes': [('NSsites'     , 8),
                            ('omega'       , 1.7),
                            ('alpha'       , '*'),
                            ('method'      , '*'),
                            ('Malpha'      , '*'),
                            ('fix_alpha'   , '*')]},
    'fb'    :  {'typ': 'branch'     , 'evol': 'free-ratios',
                'allow_mark': True , 
                'changes': [('model'       , 1),
                            ('NSsites'     , 0)]},
    'b_free':  {'typ': 'branch'     , 'evol': 'positive-selection',
                'allow_mark': True , 
                'changes': [('model'       , 2),
                            ('NSsites'     , 0)]},
    'b_neut':  {'typ': 'branch'     , 'evol': 'relaxation',
                'allow_mark': True , 
                'changes': [('model'       , 2),
                            ('NSsites'     , 0),
                            ('fix_omega'   , 1),
                            ('omega'       , 1)]},
    'bsA1'  :  {'typ': 'branch-site', 'evol': 'relaxation',
                'allow_mark': True , 
                'changes': [('model'       , 2),
                            ('NSsites'     , 2),
                            ('fix_omega'   , 1),
                            ('omega'       , 1),
                            ('ncatG'       , '*')]},
    'bsA'   :  {'typ': 'branch-site', 'evol': 'positive-selection',
                'allow_mark': True , 
                'changes': [('model'       , 2),
                            ('NSsites'     , 2),
                            ('omega'       , 1.7),
                            ('ncatG'       , '*')]},
    'bsB'   :  {'typ': 'branch-site', 'evol': 'positive-selection',
                'allow_mark': True , 
                'changes': [('model'       , 2),
                            ('NSsites'     , 3),
                            ('omega'       , 1.7),
                            ('ncatG'       , '*')]},
    'bsC'   :  {'typ': 'branch-site', 'evol': 'different-ratios',
                'allow_mark': True , 
                'changes': [('model'       , 3),
                            ('NSsites'     , 2),
                            ('ncatG'       , '*')]},
    'bsD'   :  {'typ': 'branch-site', 'evol': 'different-ratios',
                'allow_mark': True , 
                'changes': [('model'       , 3),
                            ('NSsites'     , 3),
                            ('ncatG'       , 2)]}
    }
