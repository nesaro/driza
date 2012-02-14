Descripcion
------------
El funcionamiento de driza gira en torno a una coleccion de registros. 
Cada registro tiene a su vez campos. Cada campo es de un tipo concreto, e importa el orden.
Por tanto, tambi�n existe un listado de tipos. Cada tipo tiene una serie de cualidades, como nombre y valor por defecto.

Implementaci�n
--------------

Para los registros, es suficiente con una lista.
Para los campos de cada registro, es necesario una clase basada en lista, pero que ademas tenga unas ciertas propiedades.
Para las variables, es conveniente usar una lista.

La clase principal que contenga estos componentes ha de garantizar la integridad de todas las listas.
* Si se inserta un registro, todos sus campos deben ajustarse a las variables existentes.
* Si se inserta una variable, todos los registros deben incorporar el valor por defecto de dicha variable en la posici�n que ocupe.
* Si se modifica un campo de un registro, se ha de verificar si ese campo se ajusta a la definici�n de la variable que le corresponde
* Si se modifica el tipo de una variable, deber�a existir un mecanismo de conversi�n para el campo correspondiente en todos los registros
* Si se elimina una variable, se ha de eliminar todos los campos asociados a dicha variable

Las clases
----------

Proximamente
