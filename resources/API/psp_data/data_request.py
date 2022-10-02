import pyspedas
from pytplot import tplot
import pandas as pd


spe_vars = pyspedas.psp.spe(trange=['2018-11-5', '2018-11-5/06:00'], datatype='spa_sf1_32e', level='l2', time_clip=True,
                            notplot=True, no_update=True)


columns = {'x': spe_vars['psp_spe_EFLUX']['x'],
           'y': [list(y_point) for y_point in spe_vars['psp_spe_EFLUX']['y']],
           'v': [list(v_point) for v_point in spe_vars['psp_spe_EFLUX']['v']]}

compression_opts = dict(method='zip',
                       archive_name='PSPEFLUX.csv')
formatted_data = pd.DataFrame(data=columns)
formatted_data.to_csv('PSPEFLUX.zip',columns=columns, compression=compression_opts)

