import os
import sys

from pyintegrity.common.ymlInput import ymlInput
from pyintegrity.common.update_deep import AttributeDict
from pyintegrity.common.ApplicationManager import ConfigureApplicationInputs
from pyintegrity.API579 import API579

ymlfile = 'src/pyintegrity/tests/test_data/API579/12in_oil_cml31_input.yml'
sys.argv.append(ymlfile)
print(os.path.isfile(ymlfile))
cfg = ymlInput(ymlfile, updateYml=None)
cfg = AttributeDict(cfg)

basename = 'API579'
application_manager = ConfigureApplicationInputs(basename)
application_manager.configure(run_dict=None)

cfg_base = API579(application_manager.cfg)
