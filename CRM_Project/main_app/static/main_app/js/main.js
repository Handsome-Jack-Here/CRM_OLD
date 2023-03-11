$(document).ready(function () {

    $('#save_order').attr('disabled', true)

    function getCookie(name) {
        let cookieValue = null
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';')
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim()
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                    break
                }
            }
        }
        return cookieValue
    }

    const csrftoken = getCookie('csrftoken')

    var name, surname, phone_number, brand, model, serial_number, type_of_unit, types, defect

    $('.client_edit').hide()
    $('.unit_edit').hide()
    var order = $('.order_id span').text()
    $.ajax({
        url: '/order-edit/',
        method: 'GET',
        data: {'order_id': order},
        dataType: 'json',
    }).done(function (response) {
        name = response.client.name
        surname = response.client.surname
        phone_number = response.client.phone_number
        brand = response.unit.brand
        model = response.unit.model
        serial_number = response.unit.serial_number
        type_of_unit = response.unit.type_of_unit
        types = response.types.types
        defect = response.order.defect

        for (var i in types) {
            if (types[i].unit_type == type_of_unit) {
                var item = `<option selected>${types[i].unit_type}</option>`
            } else {
                var item = `<option>${types[i].unit_type}</option>`
            }
            $('#type_of_unit').append(item)
        }


        $('#name').val(name)
        $('#surname').val(surname)
        $('#phone_number').val(phone_number)

        $('#brand').val(brand)
        $('#model').val(model)
        $('#serial_number').val(serial_number)
        $('#type_of_unit').val(type_of_unit)

        $('#defect_edit').val(defect)


        $('.client_fields').append(`<span> ${$('#name').val()} </span> <br>`)
        $('.client_fields').append(`<span> ${$('#surname').val()} </span> <br>`)
        $('.client_fields').append(`<span> ${$('#phone_number').val()} </span> <br>`)

        $('.unit_fields').append(`<span> ${$('#brand').val()} </span> <br>`)
        $('.unit_fields').append(`<span> ${$('#model').val()} </span> <br>`)
        $('.unit_fields').append(`<span> ${$('#serial_number').val()} </span> <br>`)
        $('.unit_fields').append(`<span> ${$('#type_of_unit').val()} </span> <br>`)


    })


    // click Client edit
    $('.client_static a').click(function (e) {
        e.preventDefault()
        
        $('#save_order').attr('disabled', false)
        $('.client_static').hide()
        $('.client_edit').fadeIn(140)

        // close Client edit
        $('.close_client_edit').click(function (e) {
            e.preventDefault()
            $('.client_edit').hide()
            $('.client_static').fadeIn(140)
            $('.client_fields *').remove()
            $('.client_fields').append(`<span> ${$('#name').val()}  </span> <br>`)
            $('.client_fields').append(`<span> ${$('#surname').val()}  </span> <br>`)
            $('.client_fields').append(`<span> ${$('#phone_number').val()}  </span> <br>`)
        })
    })

    // click Unit edit
    $('.unit_static a').click(function (e) {
        e.preventDefault()
        $('#type_of_unit option').remove()
        $('.unit_static').hide()
        $('.unit_edit').fadeIn(140)

        for (var i in types) {
            if (types[i].unit_type == type_of_unit) {
                var item = `<option selected>${types[i].unit_type}</option>`
            } else {
                var item = `<option>${types[i].unit_type}</option>`
            }
            $('#type_of_unit').append(item)
        }
    })

    // close Unit edit
    $('.close_unit_edit').click(function (e) {
        e.preventDefault()
        $('.unit_fields *').remove()
        $('.unit_edit').hide()
        $('.unit_static').fadeIn(140)

        $('.unit_fields').append(`<span> ${$('#brand').val()} </span> <br>`)
        $('.unit_fields').append(`<span> ${$('#model').val()} </span> <br>`)
        $('.unit_fields').append(`<span> ${$('#serial_number').val()} </span> <br>`)
        $('.unit_fields').append(`<span> ${$('#type_of_unit option').filter(':selected').val()} </span> <br>`)
        type_of_unit = $('#type_of_unit option').filter(':selected').val()
    })

    $('#save_order').click(function (e) {
        e.preventDefault()
        var data = {
            'order': order,
            'name': $('#name').val(),
            'surname': $('#surname').val(),
            'phone_number': $('#phone_number').val(),
            'brand': $('#brand').val(),
            'model': $('#model').val(),
            'serial_number': $('#serial_number').val(),
            'unit_type': $('#type_of_unit option').filter(':selected').val(),

            csrfmiddlewaretoken: csrftoken
        }
        $.ajax({
            url: '/order-edit/',
            method: 'POST',
            data: data,
        }).done(function (response) {
            alert('Order saved')
        })
    })

})


