import dash
# Libreria necesaria de DASH
import dash_core_components as dcc
# Librerias necesaria de DASH
import dash_html_components as html
# Librerias necesarias de DASH
import plotly.express as px
#Apartado grafico / funcional
import plotly.graph_objects as go
import pandas as pd
# Herramientras tratado de bases de datos
from Connection import Connection
# Clase definida enteriormente en el archivo Connection.py, es una clase para conectarse con la base de datos.
import MotorSQL as sql
# Busquedas de SQL desfinidas en covidSQL.py

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"] # Herramienta de ayuda para el diseño de la pagina/aplicacion, en este caso es BOOTSTRAP

app = dash.Dash(__name__, external_stylesheets=external_stylesheets) # App es una aplicacion y App es un objeto que es instancia de Dash | __name__ es un atributo de python el cual
#                                                                       verifica si el parametro que recibio si proviene del archivo que inicia la aplicacion.
app.layout = html.Div(
    style={'backroundColor': 'black'},
    children=[html.H1('html code')]
)


# AmountCarBrand
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.AmountCarBrand(), con.connection)
con.closeConnection()
dfGraphBrands = pd.DataFrame(query, columns=["brand", "numero_vehiculos"])
figBarBrands = px.bar(dfGraphBrands.head(41), x="brand", y="numero_vehiculos")

#Numero de vehiculos segun el motor
con.openConnection()
query = pd.read_sql_query(sql.Numero_Vehiculos_Motor(), con.connection)
con.closeConnection()
dfGraphVehMotor = pd.DataFrame(query, columns=["vehicle_motor", "amount_veh"])
figVehMotor = px.bar(dfGraphVehMotor.head(12), x="vehicle_motor", y="amount_veh")

#Cantidad de vehiculos segun el año
con.openConnection()
query = pd.read_sql_query(sql.NumeroVehiculosPYear(), con.connection)
con.closeConnection()
dfGraphVehYear = pd.DataFrame(query, columns=["vehicle_year","amount_vehicles"])
figVehYear = px.bar(dfGraphVehYear.head(12), x="vehicle_year", y="amount_vehicles")

#Cantidad de modelos, segun los mas comunes
con.openConnection()
query = pd.read_sql_query(sql.NumeroModelosMasComunes(), con.connection)
con.closeConnection()
dfGraphModelBrand = pd.DataFrame(query, columns=["brand","commun_models"])
figModelBrand = px.bar(dfGraphModelBrand.head(12), x="commun_models", y="brand")

#Cantidad baterias compradas segun marca de ka bateria
con.openConnection()
query = pd.read_sql_query(sql.CountSellsBatt(), con.connection)
con.closeConnection()
dfGraphBattBrand = pd.DataFrame(query, columns=["brand_batt","amount_boughts"])
figModelBattBrand = px.pie(dfGraphBattBrand, names="brand_batt", values="amount_boughts")

#Cantidad de baterias vendidad segun la marca del vehiculo
con.openConnection()
query = pd.read_sql_query(sql.CountSellsBrand(), con.connection)
con.closeConnection()
dfGraphBrandSells = pd.DataFrame(query, columns=["car_brand","amount_boughts"])
figModelSellsBrand = px.bar(dfGraphBrandSells.head(12), x="car_brand", y="amount_boughts")


#Cantidad baterias compradas por ciudad
con.openConnection()
query = pd.read_sql_query(sql.CountSellsPCity(), con.connection)
con.closeConnection()
dfGraphSellsCity = pd.DataFrame(query, columns=["name_city","amount_boughts_city"])
figSellsCity = px.pie(dfGraphSellsCity, names="name_city", values="amount_boughts_city")

#Cantidad baterias compradas segun modelo.
con.openConnection()
query = pd.read_sql_query(sql.CountSellsRefBatt(), con.connection)
con.closeConnection()
dfGraphSellsModel = pd.DataFrame(query, columns=["reff_batt","amount_boughts_ref_batt"])
figSellsModels = px.pie(dfGraphSellsModel, names="reff_batt", values="amount_boughts_ref_batt")





#Layout
app.layout = html.Div(children=[# Con esto se especifica que va a estar escrito el codigo de html en formato JSON, lo de los hijos es basicamente como "seciones"
    html.Span(className="container-fluid", children=[
        #Row for cases
        html.Div(className="row", children=[
            #Col for bars
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-success", children=[
                    html.Div(className="card-danger bg-success text-white", children=[
                        html.H3(children="Baterias Runno"),
                    ]),
                ]),
            ]),
        ]),
    ]),

    html.H1(children="                              "),##

    html.Span(className="container-fluid", children=[
        #Row for cases
        html.Div(className="row", children=[
            #Col for bars
            html.Div(className="col-10 col-xl-6", children=[
                html.Div(className="card border-danger", children=[
                    html.Div(className="card-success bg-danger text-light", children=[
                        html.H3(children="Numero de referencias segun la marca"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Numero vehiculos por marca",
                            figure=figBarBrands
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),

    html.H1(children="                              "),##

    html.Span(className="container-fluid", children=[
        #Row for cases
        html.Div(className="row", children=[
            #Col for bars
            html.Div(className="col-10 col-xl-6", children=[
                html.Div(className="card border-danger", children=[
                    html.Div(className="card-success bg-danger text-light", children=[
                        html.H3(children="Numero de vehiculos segun el motor"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Numero vehiculos por motor",
                            figure=figVehMotor
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),

    html.H1(children="                              "),##

    html.Span(className="container-fluid", children=[
        #Row for cases
        html.Div(className="row", children=[
            #Col for bars
            html.Div(className="col-10 col-xl-6", children=[
                html.Div(className="card border-danger", children=[
                    html.Div(className="card-success bg-danger text-light", children=[
                        html.H3(children="Numero de vehiculos segun el año"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Numero vehiculos segun el año",
                            figure=figVehYear
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),

    html.H1(children="                              "),##

    html.Span(className="container-fluid", children=[
        #Row for cases
        html.Div(className="row", children=[
            #Col for bars
            html.Div(className="col-10 col-xl-6", children=[
                html.Div(className="card border-danger", children=[
                    html.Div(className="card-success bg-danger text-light", children=[
                        html.H3(children="Numero de modelos segun la marca"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Modelos segun la marca",
                            figure=figModelBrand
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),

    html.H1(children="                              "),  ##

    html.Span(className="container-fluid", children=[
        # Row for cases
        html.Div(className="row", children=[
            # Col for bars
            html.Div(className="col-10 col-xl-6", children=[
                html.Div(className="card border-danger", children=[
                    html.Div(className="card-success bg-danger text-light", children=[
                        html.H3(children="Baterias compradas segun marcas"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Cantidad de baterias compradas segun la marca",
                            figure=figModelBattBrand
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),

    html.H1(children="                              "),  ##

    html.Span(className="container-fluid", children=[
        # Row for cases
        html.Div(className="row", children=[
            # Col for bars
            html.Div(className="col-10 col-xl-6", children=[
                html.Div(className="card border-danger", children=[
                    html.Div(className="card-success bg-danger text-light", children=[
                        html.H3(children="Baterias compradas segun la marca del vehiculo"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Marcas de vehiculos / cantidad de baterias comprada",
                            figure=figModelSellsBrand
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),

    html.H1(children="                              "),  ##

    html.Span(className="container-fluid", children=[
        # Row for cases
        html.Div(className="row", children=[
            # Col for bars
            html.Div(className="col-10 col-xl-6", children=[
                html.Div(className="card border-danger", children=[
                    html.Div(className="card-success bg-danger text-light", children=[
                        html.H3(children="Compras segun ciudades"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Baterias vendidas por ciudad",
                            figure=figSellsCity
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),

    html.H1(children="                              "),  ##

    html.Span(className="container-fluid", children=[
        # Row for cases
        html.Div(className="row", children=[
            # Col for bars
            html.Div(className="col-10 col-xl-6", children=[
                html.Div(className="card border-danger", children=[
                    html.Div(className="card-success bg-danger text-light", children=[
                        html.H3(children="Modelos de baterias compradas"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Modelos de baterias compradas",
                            figure=figSellsModels
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),






])


if __name__ == "__main__":
    app.run_server(debug=True)