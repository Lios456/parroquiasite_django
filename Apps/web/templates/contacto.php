{% extends 'base.html' %}
{% block body %}
<section id="quote" class="padding-small">
  <div class="container text-center">
    <h3 class="display-6 fw-semibold mb-4">Deja Aquí tu pregunta</h3>
    <form id="form_contacto" class="contact-form row mt-5" method="post">
      {% csrf_token %}
      <div class="col-lg-6 col-md-12 col-sm-12 mb-4">
        <input type="text" id="name" name="name" placeholder="Nombre Completo*" class="form-control w-100 ps-3 py-2 rounded-0" required>
      </div>
      <div class="col-lg-6 col-md-12 col-sm-12 mb-4">
        <input type="email" id="email" name="email" placeholder="Correo Electrónico*" class="form-control w-100 ps-3 py-2 rounded-0" required>
      </div>
      <div class="col-lg-6 col-md-12 col-sm-12 mb-4">
        <input type="text" id="phone" name="phone" placeholder="Teléfono*" class="form-control w-100 ps-3 py-2 rounded-0" required>
      </div>
      <div class="col-lg-6 col-md-12 col-sm-12 mb-4">
        <input type="text" id="address" name="address" placeholder="Dirección*" class="form-control w-100 ps-3 py-2 rounded-0" required>
      </div>
      <div class="col-md-12 col-sm-12 mb-4">
        <textarea id="message" class="form-control w-100 ps-3 py-2 rounded-0" rows="6" type="text" name="message" placeholder="Mensaje"></textarea>
      </div>
      <center>
        <button type="submit" class="btn btn-success w-50">Enviar</button>
      </center>
    </form>
  </div>
</section>

<script>
    $("#form_contacto").validate({
      rules: {
        name: {
          required: true,
          minlength: 3,
          letras: true
        },
        email: {
          required: true,
          email: true
        },
        phone: {
          required: true,
          digits: true,
          minlength: 7,
          maxlength: 15
        },
        address: {
          required: true,
          minlength: 5
        },
        message: {
          required: true,
          minlength: 10
        }
      },
      messages: {
        name: {
          required: "Por favor, ingresa tu nombre completo.",
          minlength: "El nombre debe tener al menos 3 caracteres."
        },
        email: {
          required: "Por favor, ingresa tu correo electrónico.",
          email: "Ingresa un correo válido."
        },
        phone: {
          required: "Por favor, ingresa tu número de teléfono.",
          digits: "Solo se permiten números.",
          minlength: "El teléfono debe tener al menos 7 dígitos.",
          maxlength: "El teléfono no debe superar los 15 dígitos."
        },
        address: {
          required: "Por favor, ingresa tu dirección.",
          minlength: "La dirección debe tener al menos 5 caracteres."
        },
        message: {
          required: "Por favor, ingresa un mensaje.",
          minlength: "El mensaje debe tener al menos 10 caracteres."
        }
      },
      errorElement: "div",
      errorPlacement: function (error, element) {
        error.addClass("text-danger mt-1");
        error.insertAfter(element);
      }
    });

    // Método para validar solo letras
    jQuery.validator.addMethod("letras", function(value, element) {            
      return this.optional(element) || /^[A-Za-zÁÉÍÓÚÑáéíóúñ ]*$/.test(value);
    }, "Este campo solo acepta letras.");
</script>

{% endblock %}
