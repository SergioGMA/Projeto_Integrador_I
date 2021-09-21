$(document).ready(function() {
    window.funcs = new Funcs()
    let csrftoken = funcs.getCookie('csrftoken')
    let token = "d77cf6728df102e6e6ceda0b456c9e50bec7cc3c"
    let url = "http://127.0.0.1:8000/api/vaccines/"

    // REQUEST TYPE GET
    $.ajax({
        headers: {
            'X-CSRFToken': csrftoken,
            'Authorization': `Token ${token}` 
        },
        url: url,
        type: 'GET',
        async: true,
        dataType: 'json',
        complete: function(jqXHR) {
            //console.log(jqXHR)
            if (jqXHR.status == 200) {
                let data = jqXHR.responseJSON
                console.log(data)

                let html
                for (n in data)
                    html += `<option value="${data[n]['id']}">${data[n]['name']}</option>`

                $("#list").append(html)
            }
        },
        error: function(data) {
            //console.log(data)
            alert(data.statusText)
        }
    })

    // CLICK DO BOTÃO SEND - REQUEST TYPE POST
    $(".btn").on("click", function(event) {
        event.preventDefault();
        let data = {
            "name": $("#name").val(),
            "desc": $("#desc").val(),
            "qtd_dose": parseInt($("#qtd_dose").val()),
            "lote": $("#lote").val(),
        }
        $.each($("#addVaccines input[type='text']"), function(k, v) {
            if ($(v).val().length == 0) {
                alert('Por favor, preencher todos os campos')
                return false
            }
        });

        //console.log(data)
        $.ajax({
            headers: {
                'X-CSRFToken': csrftoken,
                'Authorization': `Token ${token}`
            },
            url: url,
            data: JSON.stringify(data),
            type: 'POST',
            async: true,
            dataType: 'json',
            complete: function(jqXHR) {
                if (jqXHR.status == 200) {
                    let data = jqXHR.responseJSON
                    alert('Dados salvo com sucesso!')
                } else {
                    alert('Não foi possivel salvar os dados!')
                }
            },
            error: function(data) {
                alert(data.statusText)
            }

        })
    })
});