{% extends 'base.html' %}
{% block body %}
<section id="quote" class="padding-small">
  <div class="container text-center">
    <h3 class="display-6 fw-semibold mb-4">Deja Aquí tu pregunta</h3>
    <form class="contact-form row mt-5" method="post">
      {% csrf_token %}
      <div class="col-lg-6 col-md-12 col-sm-12 mb-4">
        <input type="text" name="name" placeholder="Nombre Completo*" class="form-control w-100 ps-3 py-2 rounded-0"
          required>
      </div>
      <div class="col-lg-6 col-md-12 col-sm-12 mb-4">
        <input type="email" name="email" placeholder="Correo Electrónico*" class="form-control w-100 ps-3 py-2 rounded-0" required>
      </div>
      <div class="col-lg-6 col-md-12 col-sm-12 mb-4">
        <input type="text" name="phone" placeholder="Teléfono*" class="form-control w-100 ps-3 py-2 rounded-0" required>
      </div>
      <div class="col-lg-6 col-md-12 col-sm-12 mb-4">
        <input type="text" name="address" placeholder="Dirección*" class="form-control w-100 ps-3 py-2 rounded-0"
          required>
      </div>
      <div class="col-md-12 col-sm-12 mb-4">
        <textarea class="form-control w-100 ps-3 py-2 rounded-0" rows="6" type="text" name="message"
          placeholder="Mensaje"></textarea>
      </div>
      <center>
        <button
          type="submit"
          class="btn btn-success w-50">
          Enviar
        </button>
      </center>

    </form>
  </div>
</section>
{% endblock%}

