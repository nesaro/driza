===========
Undo y Redo
===========

Implementaci�n
--------------

Las operaciones de inserci�n o extracci�n de variables o registros seran objetos de una clase que herede de otra clase base llamada "transaccion"
Cada operacion (transaccion) tendra un m�todo para volver al estado anterior. Por este motivo, en algunos casos almacenara ciertos datos (que hab�a en esa posici�n anteriormente, por ejemplo).

Una pila almacenar� las transacciones, permitiendo al usuario a trav�s del undo y del redo recuperar un estado anterior
