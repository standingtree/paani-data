'''Helper functions used elsewhere in the codebase.'''


def line_to_grid(linear_range=[0, 1, 2, 3], grid_shape=[2, 3]):
    '''Return a list of 2-D coordinates corresponding to a each element of a 1-D array/list of objects, in shape = grid_shape
    Useful for converting a linear index into a coordinate grid for charting purposes. Note that elements of
    linear range that do not fit in a grid of shape = grid_shape will be truncated.
    Arguments:
    | -- linear_range, list of ints: input indexes to be converted to a 2-d grid.
    | -- grid_shape, tuple of ints: the shape of the coordinate grid returned
    Returns:
        a dict with keys = indexes of the linear_range, and values = grid coordinates.
    '''
    # make a list of indices for the linear_range
    linear_range = [_ for _ in dict(enumerate(linear_range))]
    grid_coords = []
    for r in range(grid_shape[0]):
        for c in range(grid_shape[1]):
            grid_coords.append((r, c))

    return dict(zip(linear_range, grid_coords))



import matplotlib.pyplot as plt
def quickplot(data, plot_title='', ylabel='', xlabel='', legend=[], yaxisformat="{x:,.2f}"):
    '''Outputs a single quick, nicely formatted line chart for the passed data.'''

    fig, ax = plt.subplots(1,1, figsize=(10,5))
    ax.plot(data)
    ax.set_ylabel(ylabel)
    plt.xlabel(xlabel)
    ax.set_title(plot_title)
    #     ax.xaxis.set_major_locator(tkr.MultipleLocator())
    ax.xaxis.set_major_locator(tkr.MaxNLocator(10))
    ax.yaxis.set_major_formatter(yaxisformat)
    if len(legend)>0:
        ax.legend(legend)
    ax.grid()
    plt.show()



def get_state_codes():
    '''Returns a dict of states and their 3-letter acronyms. Note that these state codes
    do not necessarily correspond to official Indian state abbreviations.'''

    sc = {
        'Andhra Pradesh': 'ANP',
        'Arunachal Pradesh': 'ARP',
        'Assam': 'ASS',
        'Bihar': 'BIH',
        'Chhattisgarh': 'CHH',
        'Delhi': 'DEL',
        'Gujarat': 'GUJ',
        'Haryana': 'HAR',
        'Himachal Pradesh': 'HIP',
        'Jammu & Kashmir': 'JAK',
        'Jharkhand': 'JHA',
        'Karnataka': 'KAR',
        'Kerala': 'KER',
        'Madhya Pradesh': 'MAP',
        'Maharashtra': 'MAH',
        'Manipur': 'MAN',
        'Meghalaya': 'MEG',
        'Mizoram': 'MIZ',
        'Nagaland': 'NAG',
        'Odisha': 'ODI',
        'Punjab': 'PUN',
        'Rajasthan': 'RAJ',
        'Sikkim': 'SIK',
        'Tamil Nadu': 'TAM',
        'Telangana': 'TEL',
        'Tripura': 'TRI',
        'Uttar Pradesh': 'UTP',
        'Uttarakhand': 'UTT',
        'West Bengal': 'WBE',
        'Goa': 'GOA',
        'Ladakh': 'LAD'
    }
    sc = {k.upper(): v for k, v in sc.items()}
    return sc



def get_state_name(state_code: str):
    '''Returns the state codes and flip keys/values.'''
    sc = {v: k for k, v in get_state_codes().items()}
    # return the state name (upper case)
    return sc[state_code].upper()



def anonymize_states(state_codes: dict):
    '''Anonymizes state names.
    :arg state_codes: dictionary of state codes, accessed by calling the get_state_codes() function'''
    anon_root = 'State_'
    anon_sc = {}
    for i, (k, v) in enumerate(state_codes.items()):
        anon_sc[k] = anon_root + str(i + 1)

    return anon_sc



def get_basin_codes():
    '''Returns a dict of river basin names and 3-letter codes.'''
    bc = {
        'Brahmani and Baitarni': 'BAB',
        'Barak and others': 'BAR',
        'Brahamaputra': 'BRA',
        'Cauvery': 'CAU',
        'Ganga': 'GAN',
        'Godavari': 'GOD',
        'Indus (up to border)': 'IND',
        'West flowing rivers of Kutch and Saurashtra including Luni': 'KAS',
        'Krishna': 'KRI',
        'Minor rivers draining into Myanmar and Bangladesh': 'MAB',
        'Mahi': 'MAH',
        'East flowing rivers between Mahanadi and Pennar': 'MAP',
        'Narmada': 'NAR',
        'Area of North Ladakh not draining into Indus basin': 'NLA',
        'East flowing rivers between Pennar and Kanyakumari': 'PAK',
        'Pennar': 'PEN',
        'Area of inland drainage in Rajasthan': 'RAJ',
        'Sabarmati': 'SAB',
        'Subernarekha': 'SUB',
        'Tapi': 'TAP',
        'West flowing rivers from Tadri to Kanyakumari': 'TTK',
        'West flowing rivers from Tapi to Tadri': 'TTT'
    }

    bc = {k.upper(): v for k, v in bc.items()}
    return bc



def get_basin_name(basin_code: str):
    '''Returns the basin name for a passed basin code.'''
    # get the basin codes and flip keys/values
    sc = {v: k for k, v in get_basin_codes().items()}
    # return the basin name (upper case)
    return sc[basin_code].upper()


def anonymize_basins(basin_codes: dict):
    '''Takes the dictionary of basin codes and returns an anonymized dict with the same keys and new values.'''
    anon_root = 'Basin_'
    anon_bc = {}
    for i, (k, v) in enumerate(basin_codes.items()):
        anon_bc[k] = anon_root + str(i + 1)

    return anon_bc

