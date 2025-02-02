{% extends 'base.html' %}

{% block body %}
{% if user.is_superuser %}
<center>
  <h1 class="h1">Nueva Noticia</h1>
</center>
<div class="container-lg d-flex justify-content-center">
  <form method="post" name="noticiaform">
    {% csrf_token %}
    <div class="row m-3">
      <input type="text" class="form-control" name="titulo" placeholder="Título" required value="{{n.titulo}}">
    </div>
    <div class="container m-3">
      <textarea id="summernote" name="detalle" required>{{n.contenido}}</textarea>
    </div>
    
    <button type="submit" class="btn btn-success">Guardar</button>
  </form>
</div>
<div class="container-lg d-flex justify-content-center">
  <div class="table-responsive">
  <table class='table jquery'>
        <thead>
          <tr>
            <th>Título</th>
            <th>Contenido</th>
            <th>Fecha de subida</th>
            <th>Autor</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {% for n in noticias %}
            <tr>
              <td>{{n.titulo}}</td>
              <td>{{n.contenido|safe}}</td>
              <td>{{n.fecha}}</td>
              <td>{{n.autor}}</td>
              <td>
                  <a href="/new/edit/{{n.id}}" class="btn btn-warning">Editar</a>
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
  </div>
</div>
<br><br><br><br><br>


<script>
  $('#summernote').summernote({
    placeholder: 'Escribe aquí tu noticia',
    tabsize: 2,
    height: 500,
    width: 1000,
    lan: 'es-ES'
  });


</script>
{% endif %}
<div class="container">
  {% for n in noticias %}
    <div class="border border-1 row text-center m-5 p-5">
      <h2>{{n.titulo}}</h2>
      <div class="container-lg"> 
        {{ n.contenido|safe }}
      </div>
      <div class="d-flex justify-content-center mt-3 mb-3">
        <a href="/new/{{n.id}}" class="btn btn-outline-warning w-25 p-1" >Ver mas</a>
      </div>
      <div class="row">
        {{n.fecha}}
      </div>
    </div>
  {% endfor %}
</div>

{% endblock  %}