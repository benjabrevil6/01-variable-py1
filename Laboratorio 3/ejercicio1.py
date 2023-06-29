habitantes_rios = 404432
superficie_rios = 18429
habitantes_magallanes = 166533
superficie_magallanes = 1382291

densidad_ríos = habitantes_rios / superficie_rios
densidad_magallanes = habitantes_magallanes / superficie_magallanes


censo2017 = {
    14: { 
        "nombre1": "Los Ríos",
        "superficie1": "18.429",
        "habitantes1": "404.432",
    },
    12: {
        "nombre2": "Magallanes",
        "superifice2": "1.382.291",
        "habitantes2": "166.533",
    }
}
   
censo2017[14]["densidad1"] = (" {0:.1f}".format (densidad_ríos))
censo2017[12]["densidad2"] = (" {0:.1f}".format (densidad_magallanes))
censo2017[14]["capital1"] = "Valdivia"
censo2017[12]["capital2"] = "Punta Arenas"
censo2017[14]["comunas1"] = "Río Bueno, La Unión, Paillaco"
censo2017[12]["comunas2"] = "Cabo de Hornos, Puerto Williams, Porvenir"
censo2017[14]["provincias1"] = "Ranco, Valdivia"
censo2017[12]["provincias2"] = "Antártica Chilena, Magallanes, Tierra del Fuego, Última Esperanza"

print (censo2017)