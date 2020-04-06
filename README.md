<HEAD>Mis Notas</HEAD>
<H1>Una simple aplicación para tomar notas.</H1>
  
Fernando Souto (donanpher@gmail.com)  
A Coruña, Abril 2020 (durante la cuarentena del coronavirus covid-19)  


03-04-2020	Fer
	v.1.0: Funcionalidad básica hecha y comprobada.
	Mi primera aplicación hecha en PyQt5.
	Como había que hacer algo, ahora que estoy encerrado por lo del Coronavirus, decidí hacer la más simple aplicación con uso de bb.dd.
	. creado un ejecutable con pyinstaller (le llevó 3 min. 10 seg. y genera un ejecutable de 46,3 MB):
		`$ pyinstaller --onefile --windowed --add-data="misnotas.db:." misnotas.py`
		A pesar de haberle pasado --add-data="misnotas.db:." al final no me incluye la bb.dd, solo un ejecutable misnotas
		Lógico por otra parte, pues le estoy diciendo que me construya --onefile
		No hay problema, porque al distribuirlo en un zip, se pondrían los 2 archivos, el ejecutable y el .db

06-04-2020	Fer
	v.1.1 Características nueva versión:
	[x] comprobar existencia bb.dd. y si no existe, crearla y añadir 1 reg. de muestra
	[x] conseguir poner el label inferior de mensajes en rojo
	[ ] ponerle iconos a los botones
	[x] poner un label que muestre el total de notas
	[x] ocultar columna ID y añadir columna TAGLABEL|CODIGO o algo similar para añadir un campo codificable de texto(10)
	[x] añadir botón para buscaar por ese la columna activa
	[x] añadido messagebox con los créditos al darle click a la imágen del bloc de notas
	[x] diversos retoques: tamaño fijo de la ventana, etc...
	[ ] comprobar si se puede cambiar pyside2
	[x] después de buscar algo, queda el TableWidget filtrado con los resultados de la búsqueda. 
		Si se vuelve a buscar y se cancela, hago una recarga de todos los registros, pero ahora
		he metido al botón buscar un modo conmutado, es decir, cambia entre Buscar/Actualizar,
		en función de si se ha hecho una búsqueda o no.
	[x] pyinstaller no me incluye las imágenes/iconos...hay que crear un resource...
		Creado el recurso pero al ejecutar la app. da un error: No module named 'logoNotas_qrc'
		Solución: hay que compilar el recurso igual que el ui: `$ pyrcc5 logoNotas.qrc -o logoNotas_rc.py`
		Al ejecutar la aplicación, me sale el icono elegido, tanto en el label como como icono de aplicación, pero
		cuando empaqueto la aplicación con pyinstaller, el icono de la aplicación no aparece.
	[ ] Doy por concluida esta versión y dejo para más adelante investigar por qué pyinstaller no incluye el icono de aplicación

		

