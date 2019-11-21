// YA FUNCIONA
$(document).ready(function () {
    $('.addbutton').click(function () {
        let newCommand = $(this).closest('#action').clone().children().remove().end().text() 
        // dentro del gui hay un boton que tiene clase addbutton, document.ready siempre esta escuchando, rec: unity frame
        // document.ready esta listening a la clase .addButton, declaración de newCommand 
        // $ crea un objeto o variable o lo que sea con las características que le sigan
        //$ = li.closest, entonces establecemos un "action" como id. para no agarrar otras ocurrencias de la clase se establece con action
        // .children = los child elements ES UN FOR LOOP, remove() lo quita uno por uno, cierra() el children loop, text() si no esta enviaría toda la linea, solo quiero el text.OBSEVACION: si queres ingresar algun texto es .val no .text
        console.log(newCommand);
        if (newCommand && newCommand.length > 0) { // newCommand retorna si exste y se puede interpretar como boolean y es operable.
            // lengh revisa se es string y checkea la logitud del string.
            $.post('/save-command', { command: newCommand }, function (data, status) { // esto le mando al push de server.js 
                // $.post busca en el js original
                // DATA es un node object, STATUS es un status code.
                console.log(`${data.message} and status is ${status}`)
                // alert(data.message)
                setTimeout(function () {
                    location.reload(); // no hay location.href, esto refresca la página. 
                }, 100); // REFRESCA LA PAGINA DESPUES DE 100 MILISEGUNDOS
            })
        }
        else {
            console.log("error")
        }
    })
})


// YA FUNCIONA
$(document).ready(function () {
    $('.deletebutton').click(function () {
        let someCommand = $(this).closest('#target').clone().children().remove().end().text();
        $(this).closest('#target').remove();
        $.post('/delete-command', { command: someCommand }, function (data, status) {
            console.log(`${data.message} and status is ${status}`);
            // alert(data.message)
        })
    })
})

// TERMINADO
$(document).ready(function () {
    $('.clearbutton').click(function () {
        var e = document.querySelector("#list"); // regresa todos los objetos o lineas que tengan el id #list.

        //e.firstElementChild can be used. 
        var child = e.lastElementChild;
        while (child) {
            e.removeChild(child);
            child = e.lastElementChild;
        }
        $.post('/delete-all', function (data, status) {
            console.log(`${data.message} and status is ${status}`)
            // alert(data.message)
        })
    })
})

// TERMINADO
$(document).ready(function () {
    $('.submitbutton').click(function () {
        window.location.assign("/postdata");
        setTimeout(function () {
            window.location.assign("/"); // Not quite right yet.
        }, 5); // 5 es el tiempo estimado que necesitan los dos scripts para poder ejecutar eso.
        // window.location.assign("/");
        // location.reload();
    })
})

// $(document).ready(function() {
//     $('.clearbutton').click(function() {
//         $("#target").each(function(i) {
//             console.log(`$(this).closest('#target')`)
//             $(this).closest('#target').remove()
//             $.post('/delete-command', {command:Command}, function(data, status) {
//                 console.log(`${data.message} and status is ${status}`)
//                 // alert(data.message)
//             })
//         })
//     })
// })


// // YA FUNCIONA
// $(document).ready(function() {
//     $('.submittocommandlist').click(function() {
//         let newText = $('#inlineFormInput.form-control.mb-2').val()
//         console.log(newText);
//         if (newText && newText.length > 0) {
//             $.post('/save-text', {text:newText}, function(data, status) {
//                 console.log(`${data.message} and status is ${status}`)
//                 // alert(data.message)
//                 setTimeout(function() {
//                     location.reload();
//                 }, 100);
//             })
//         }
//         else {
//             console.log("error")
//         }
//     })
// })