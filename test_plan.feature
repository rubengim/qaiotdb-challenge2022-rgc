Feature: The Rick and Morty API

Scenario: Realizar peticion de character
  Given Dado el endpoint https://rickandmortyapi.com/api/character
  When Buscamos id 1
  Then La respuesta es 200
  And El contenido de la respuesta es el siguiente json
    {json}

Scenario: Realizar peticion de character no valido
  Given Dado el endpoint https://rickandmortyapi.com/api/character
  When Buscamos id 100000000
  Then La respuesta es 404

Scenario: Realizar peticion de busqueda de personaje
  Given Dado el endpoint https://rickandmortyapi.com/api/character/?name
  When Buscamos el string rick
  Then La respuesta es 200
  And Devuelve 20 resultados

Scenario: Realizar peticion de busqueda de personaje con un usuario autenticado
  Given Dado un usuario y contraseña validos
    And Dado el endpoint https://rickandmortyapi.com/api/character/?name
  When Buscamos el string rick
  Then La respuesta es 200
    And Devuelve 20 resultados

Scenario: Realizar peticion de busqueda de personaje con un usuario autenticado con credenciales invalidas
  Given Dado un usuario y contraseña invalidos
    And Dado el endpoint https://rickandmortyapi.com/api/character/?name
  When Buscamos el string rick
  Then La respuesta es 200
    And Devuelve 20 resultados