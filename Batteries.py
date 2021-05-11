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



# AmountCarBrand
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.AmountCarBrand(), con.connection)
con.closeConnection()
dfGraphBrands = pd.DataFrame(query, columns=["brand", "numero_vehiculos"])
figBarBrands = px.bar(dfGraphBrands.head(41), x="brand", y="numero_vehiculos")



# cantidad en fecha 2004-2014
con.openConnection()
query = pd.read_sql_query(sql.AmountCarsByDateRange(), con.connection)
con.closeConnection()
dfGraphBrandsYear = pd.DataFrame(query, columns=["brand", "Numero_Veh_in_brand"])
figBarBrandsYear = px.bar(dfGraphBrandsYear.head(12), x="brand", y="Numero_Veh_in_brand")

# Car Search
#con.openConnection()
#query = pd.read_sql_query(sql.ExampleCarSearch, con.connection)
#con.closeConnection()
#dfCS = pd.DataFrame(query, columns=["id","LTH", "GONHER", "CALE", "TITAN"])
#figTabCS = go.Figure(data=[go.Table(
#    header = dict (values = list(dfCS.columns), fill_color = 'blue',align = 'left'),
#    cells = dict (values = [dfCS.id, dfCS.LTH, dfCS.GONHER, dfCS.CALE, dfCS.TITAN], fill_color = 'red', align = 'left'))])





#Layout
app.layout = html.Div(children=[# Con esto se especifica que va a estar escrito el codigo de html en formato JSON, lo de los hijos es basicamente como "seciones"
    html.Div(className="container-fluid", children=[
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

    html.H1(children="                              "),

    html.Div(className="container-fluid", children=[
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

    html.H1(children="                              "),

    html.Div(className="container-fluid", children=[
        #Row for cases
        html.Div(className="row", children=[
            #Col for bars
            html.Div(className="col-10 col-xl-6", children=[
                html.Div(className="card border-danger", children=[
                    html.Div(className="card-success bg-danger text-light", children=[
                        html.H3(children="Numero de referencias segun la marca y pertenecientes al rango de años 2004-2014"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="numero de vehiculos de cierta marca segun rango de tiempo",
                            figure=figBarBrandsYear
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),





])


if __name__ == "__main__":
    app.run_server(debug=True)