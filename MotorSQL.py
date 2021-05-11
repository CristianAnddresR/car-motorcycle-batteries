def AmountCarBrand():
    return """select c_ref.vehicle_brand as brand, count(c_ref.id) as Numero_Vehiculos
            from car_references c_ref join brand on (brand.id = c_ref.id_brand)
            group by c_ref.vehicle_brand
            order by Numero_Vehiculos asc"""

def AmountCarsByDateRange():
    return """select c_ref.vehicle_brand as brand, count(c_ref.id) as Numero_Veh_in_brand
            from car_references c_ref
            where c_ref.vehicle_year = '2004 - 2014'
            group by c_ref.vehicle_brand
            order by Numero_Veh_in_brand asc"""






def ExampleCarSearch():
    return """select id, "LTH", "GONHER", "CALE", "TITAN"
            from car_references c_ref
            where c_ref.vehicle_brand = 'SUZUKI' and c_ref.vehicle_model = 'SWIFT 1.3L' and c_ref.vehicle_year = '1989 - 2014' and c_ref.vehicle_motor = '4 CIL'"""

def SixCilCatalogue():
    return """select id, vehicle_brand as Brand, vehicle_model as Model, vehicle_year as Year_Range, vehicle_motor as Motor_Type, "LTH", "GONHER", "CALE", "TITAN"
            from car_references c_ref
            where c_ref.vehicle_motor = '6 CIL'"""

def SearchGONHERbatt():
    return """select id, vehicle_brand as Brand, vehicle_model as Model, vehicle_year as Year_Range, vehicle_motor as Motor_Type, "GONHER"
            from car_references c_ref
            where "GONHER" = 'G-48-700'"""

def SearchGONHERandLTHbatt():
    return """select id, vehicle_brand as Brand, vehicle_model as Model, vehicle_year as Year_Range, vehicle_motor as Motor_Type, "LTH", "GONHER"
            from car_references c_ref
            where "GONHER" = 'G-48-700' and "LTH" = 'L-48/91-600'"""

