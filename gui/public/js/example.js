// YA FUNCIONA
$(document).ready(function() {
    $('.addbutton').click(function() {
        let newCommand = $(this).closest('#action').clone().children().remove().end().text()
        console.log(newCommand);
        if (newCommand && newCommand.length > 0) {
            console.log('yeah')
            $.post('/save-command', {command:newCommand}, function(data, status) {
                console.log(`${data.message} and status is ${status}`)
                // alert(data.message)
                setTimeout(function() {
                    location.reload();
                }, 100);
            })
        }
        else {
            console.log("error")
        }
    })
})

// YA FUNCIONA
$(document).ready(function() {
    $('.deletebutton').click(function() {
        let someCommand = $(this).closest('#target').clone().children().remove().end().text()
        let Command = someCommand//.replace(" ", "")
        console.log(Command);
        $(this).closest('#target').remove()
        $.post('/delete-command', {command:Command}, function(data, status) {
            console.log(`${data.message} and status is ${status}`)
            // alert(data.message)
        })
    })
})

// TODAVIA NO ESTA TERMINADO
$(document).ready(function() {
    $('.clearbutton').click(function() {
        var e = document.querySelector("#list"); 
        
        //e.firstElementChild can be used. 
        var child = e.lastElementChild;  
        while (child) { 
            e.removeChild(child); 
            child = e.lastElementChild; 
        }
        $.post('/delete-all', function(data, status) {
            console.log(`${data.message} and status is ${status}`)
            // alert(data.message)
        })
    })
})

// TERMINADO
$(document).ready(function() {
    $('.submitbutton').click(function() {
        window.location.assign("/postdata");
        setTimeout(function() {
            window.location.assign("/"); // Not quite right yet.
        }, 5);
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

