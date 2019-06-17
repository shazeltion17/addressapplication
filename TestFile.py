import pyap
from flask import jsonify, Flask, request, render_template
import pandas as pd
import connect_to_Database as cd


def addresser():

    #test_address = "Lorem ipsum 225 E. John Carpenter Freeway, Suite 1500 Irving, Texas 75062 Dorem sit amet + 1733 Kellogg Springs Dr. Atlanta, GA 30338 "
    test_address = request.form.get("address")
    # test_address = request.get_json(force=True)
    addresses = pyap.parse(test_address, country='US')
    print(addresses)
    if not addresses:
        data = 'There is no addresses present'
        return jsonify(data)
    full_street = []
    state = []
    street_number = []
    street_name = []
    zip_code = []
    for address in addresses:

        # shows found address
        # shows address parts
        full_address = address.as_dict()
        full_street.append(full_address['full_street'])
        zip_code.append(full_address['postal_code'])
        state.append(full_address['region1'])
        street_number.append(full_address['street_number'])
        street_name.append(full_address['street_name'])


    full_street = pd.Series(full_street)
    state = pd.Series(state)
    street_name = pd.Series(street_name)
    street_number = pd.Series(street_number)
    zip_code = pd.Series(zip_code)
    full_street.name = 'full_street'
    state.name = 'state'
    zip_code.name = 'zip_code'
    street_name.name = 'street_name'
    street_number.name = 'street_name'
    data = pd.DataFrame(pd.concat(
        [full_street, state, zip_code, street_name, street_number], axis=1, sort=False))
    cd.get_data(data)
    return jsonify(full_address)

addresser()