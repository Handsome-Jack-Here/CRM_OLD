$(document).ready(function () {
    $('.client_edit').hide()
    var data = $('.order_id span').text()
    $.ajax({
        url: '/order-edit/',
        method: 'GET',
        data: {'order_id': data},
        dataType: 'json',
    }).done(function (response) {
        $('.client_fields').append(`${response.client.name} <br>`)
        $('.client_fields').append(`${response.client.surname} <br>`)
        $('.client_fields').append(`${response.client.phone_number} <br>`)
    })

    // click edit
    $('.client_static a').click(function (e) {
        e.preventDefault()
        $('.client_static').fadeToggle()
        $('.client_edit').fadeIn(10)
        var data = $('.order_id span').text()
        $.ajax({
            url: '/order-edit/',
            method: 'GET',
            data: {'order_id': data},
            dataType: 'json',
        }).done(function (response) {
            $('#name').val(response.client.name)
            $('#surname').val(response.client.surname)
            $('#phone_number').val(response.client.phone_number)

            $('#client_edit').submit(function (e){
                e.preventDefault()
                alert('Saved')
            })
        })
    })

})