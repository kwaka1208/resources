function copyToClipboard(text) {
  const el = document.createElement("textarea");
  el.value = text;
  el.setAttribute("readonly", "");
  el.style.position = "absolute";
  el.style.left = "-9999px";
  document.body.appendChild(el);
  el.select();
  document.execCommand("copy");
  document.body.removeChild(el);
  showToast();
}

let toastTimeout;
function showToast() {
  const toast = document.getElementById("toast");
  toast.classList.remove("hidden");
  toast.classList.remove("toast");
  void toast.offsetWidth;
  toast.classList.add("toast");
  clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => {
    toast.classList.add("hidden");
    toast.classList.remove("toast");
  }, 2000);
}
