$(document).ready(function() {
    $('.send').click(function() {
        let newCommand = $('#action').val()
        console.log(newCommand);
        if (newCommand && newCommand.length > 0) {
            console.log('yeah')
            $.post('/save-command', {command:newCommand}, function(data, status) {
                console.log(`${data.message} and status is ${status}`)
                alert(data.message)
                setTimeout(function() {
                    location.reload();
                }, 500);
            })
        }
        else {
            console.log("error")
        }
    })
})

$(document).ready(function() {
    $('.delete').click(function() {
        let someCommand = $(this).closest('#target').clone().children().remove().end().text()
        let Command = someCommand.replace(" ", "")
        console.log(Command);
        $(this).closest('#target').remove()
        $.post('/delete-command', {command:Command}, function(data, status) {
            console.log(`${data.message} and status is ${status}`)
            alert(data.message)
        })
    })
})
