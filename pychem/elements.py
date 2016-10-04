f_obj = open('elements.csv')
element_line_list = f_obj.readlines()

for line in element_line_list:
    element_details = line.split(',')
    (atomic_number,
     symbol,
     name,
     atomic_mass,
     color,
     electronic_config,
     electronegativity,
     atomic_radius,
     ionic_radius,
     van_der_waals,
     ionization_energy,
     electron_affinity,
     standard_state,
     bonding_type,
     melting_point,
     boiling_point,
     density,
     acidity,
     year_discovered) = element_details

    mapped_details = {'atomic_number': atomic_number,
                        'symbol': symbol,
                        'name': name,
                        'atomic_mass': atomic_mass,
                        'color': color,
                        'electronic_config': electronic_config,
                        'electronegativity': electronegativity,
                        'atomic_radius': atomic_radius,
                        'ionic_radius': ionic_radius,
                        'van_der_waals': van_der_waals,
                        'ionization_energy': ionization_energy,
                        'electron_affinity': electron_affinity,
                        'standard_state': standard_state,
                        'bonding_type': bonding_type,
                        'melting_point': melting_point,
                        'boiling_point': boiling_point,
                        'density': density,
                        'acidity': acidity,
                        'year_discovered': year_discovered}

    elements = {symbol: mapped_details}


def get_from_symbol(symbol):
    for symbol, details in elements.items():
        if symbol in elements.keys():
            print(elements[symbol])


get_from_symbol('Li')

