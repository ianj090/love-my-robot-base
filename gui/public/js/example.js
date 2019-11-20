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
        let Commands = $(".target").text()
        $(".target").empty();
        console.log("Commands")
        $.post('/delete-all', {command:Commands}, function(data, status) {
            console.log(`${data.message} and status is ${status}`)
            // alert(data.message)
        })
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

