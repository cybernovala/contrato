document.addEventListener("DOMContentLoaded", () => {
  const hoy = new Date().toISOString().split("T")[0];
  document.getElementById("fecha").value = hoy;
  document.getElementById("inicio").value = hoy;
});

document.getElementById("formulario").addEventListener("submit", async (e) => {
  e.preventDefault();

  const form = new FormData(e.target);
  const data = {};
  for (const [key, value] of form.entries()) {
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
});
