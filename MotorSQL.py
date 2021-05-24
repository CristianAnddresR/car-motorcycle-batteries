def AmountCarBrand():#BAR
    return """select c_ref.vehicle_brand as brand, count(c_ref.id) as Numero_Vehiculos
            from car_references c_ref
            group by c_ref.vehicle_brand
            order by Numero_Vehiculos desc"""

def Numero_Vehiculos_Motor():#BAR
    return """select distinct c_ref.vehicle_motor, count(c_ref.id) as amount_veh
            from car_references as c_ref
            group by c_ref.vehicle_motor
            order by amount_veh desc"""

def NumeroVehiculosPYear():#BAR
    return """select distinct c_ref.vehicle_year, count(c_ref.id) as amount_vehicles
            from car_references as c_ref
            group by c_ref.vehicle_year
            order by amount_vehicles desc"""


def NumeroModelosMasComunes():#BAR
    return """select c_ref.vehicle_model as brand, count(c_ref.id) as commun_models
            from car_references c_ref
            group by c_ref.vehicle_model
            order by commun_models desc"""

def CountSellsBatt():#PIE
    return """select distinct cp.brand_batt, count(cp.id) as amount_boughts
            from compras_pasadas as cp
            group by cp.brand_batt
            order by amount_boughts desc"""

def CountSellsBrand():#BAR
    return """select distinct cp.car_brand, count(cp.id) as amount_boughts
            from compras_pasadas as cp
            group by cp.car_brand
            order by amount_boughts desc"""

def CountSellsPCity():#PIE
    return """select distinct citys.name_city, count(cp.id) as amount_boughts_city
            from compras_pasadas as cp join citys on (cp.id_citys = citys.id)
            group by citys.name_city
            order by amount_boughts_city desc"""

def CountSellsRefBatt():#PIE
    return """select distinct cp.reff_batt, count(cp.id) as amount_boughts_ref_batt
            from compras_pasadas as cp
            group by cp.reff_batt
            order by amount_boughts_ref_batt desc"""





