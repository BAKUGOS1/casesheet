/* Kiosk interactions: selection states, consent switches and the microphone
   affordance. Presentation only — nothing is submitted anywhere. */
(function () {
  "use strict";

  /* Consent switches ------------------------------------------------------ */
  document.addEventListener("click", function (event) {
    var row = event.target.closest("[data-consent]");
    if (row) {
      if (row.getAttribute("data-required") === "true") return;
      row.classList.toggle("is-on");
      var toggle = row.querySelector(".switch");
      if (toggle) toggle.setAttribute("aria-checked", row.classList.contains("is-on") ? "true" : "false");
      return;
    }

    /* Single-choice tiles (complaints, interview options) ------------------ */
    var tile = event.target.closest("[data-choice]");
    if (tile) {
      var group = tile.closest("[data-choice-group]");
      if (group && group.getAttribute("data-multi") !== "true") {
        group.querySelectorAll("[data-choice]").forEach(function (other) {
          other.classList.remove("is-selected");
        });
      }
      tile.classList.toggle("is-selected");
      var echo = document.querySelector("[data-choice-echo]");
      if (echo) echo.textContent = tile.getAttribute("data-choice");
      return;
    }

    /* Microphone ----------------------------------------------------------- */
    var mic = event.target.closest("[data-mic]");
    if (mic) {
      var listening = !mic.classList.contains("is-idle");
      mic.classList.toggle("is-idle", listening);
      var label = document.querySelector("[data-mic-label]");
      if (label) label.textContent = listening ? "Tap to speak" : "Listening";
      return;
    }

    /* Body map ------------------------------------------------------------- */
    var region = event.target.closest("[data-region]");
    if (region) {
      var caption = document.querySelector("[data-region-caption]");
      if (caption) caption.textContent = "Selected: " + region.getAttribute("data-region");
    }
  });
})();
