document.addEventListener("DOMContentLoaded", () => {
  const hoy = new Date().toISOString().split("T")[0];
  document.getElementById("fecha").value = hoy;
  document.getElementById("inicio").value = hoy;
});

function mostrarVistaPrevia() {
  const form = document.getElementById("formulario");
  const vista = document.getElementById("vista-previa");
  const formVista = document.getElementById("form-vista-previa");

  formVista.innerHTML = ""; // Limpiar

  const formData = new FormData(form);
  for (const [key, value] of formData.entries()) {
    const label = document.createElement("label");
    label.textContent = `${key.replaceAll("_", " ")}:`;

    const input = document.createElement("input");
    input.name = key;
    input.value = value;
    input.required = true;

    label.appendChild(input);
    formVista.appendChild(label);
  }

  form.classList.add("hidden");
  vista.classList.remove("hidden");
}

function modificar() {
  document.getElementById("vista-previa").classList.add("hidden");
  document.getElementById("formulario").classList.remove("hidden");
}

async function generarPDF() {
  const formVista = document.getElementById("form-vista-previa");
  const formData = new FormData(formVista);
  const data = {};
  for (const [key, value] of formData.entries()) {
    data[key] = value;
  }

  try {
    const response = await fetch("https://contrato-backend.onrender.com/generar_pdf", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    if (!response.ok) throw new Error("Error en el servidor");

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "contrato.pdf";
    a.click();
    window.URL.revokeObjectURL(url);
  } catch (error) {
    alert("Error al generar el contrato.");
  }
}
