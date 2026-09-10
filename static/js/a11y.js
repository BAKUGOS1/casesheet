/* Accessibility controls shared by every surface.
   Plain browser JavaScript, no framework, no build step. */
(function () {
  "use strict";

  var root = document.documentElement;
  var TEXT_STEPS = ["normal", "large", "xlarge"];
  var TEXT_LABELS = { normal: "Text size", large: "Bigger text", xlarge: "Biggest text" };

  function read(key, fallback) {
    try {
      return window.localStorage.getItem(key) || fallback;
    } catch (err) {
      return fallback;
    }
  }

  function write(key, value) {
    try {
      window.localStorage.setItem(key, value);
    } catch (err) {
      /* private browsing or blocked storage: the preference just will not stick */
    }
  }

  function applyText(size) {
    root.setAttribute("data-text", size);
    var label = document.querySelector("[data-text-label]");
    if (label) label.textContent = TEXT_LABELS[size];
  }

  function applyContrast(mode) {
    root.setAttribute("data-contrast", mode);
    var button = document.querySelector("[data-toggle-contrast]");
    if (button) button.setAttribute("aria-pressed", mode === "high" ? "true" : "false");
  }

  function applyAudio(state) {
    var button = document.querySelector("[data-toggle-audio]");
    var label = document.querySelector("[data-audio-label]");
    if (button) button.setAttribute("aria-pressed", state === "on" ? "true" : "false");
    if (label) label.textContent = state === "on" ? "Audio on" : "Audio off";
  }

  /* ?contrast=high and ?text=large let a demo or a screenshot open a screen
     directly in an accessibility mode, without touching the stored preference. */
  var params = new URLSearchParams(window.location.search);
  var textParam = params.get("text");
  var contrastParam = params.get("contrast");

  applyText(TEXT_STEPS.indexOf(textParam) > -1 ? textParam : read("cs-text", "normal"));
  applyContrast(contrastParam === "high" ? "high" : read("cs-contrast", "normal"));
  applyAudio(read("cs-audio", "on"));

  document.addEventListener("click", function (event) {
    var textButton = event.target.closest("[data-toggle-text]");
    if (textButton) {
      var next = TEXT_STEPS[(TEXT_STEPS.indexOf(root.getAttribute("data-text")) + 1) % TEXT_STEPS.length];
      applyText(next);
      write("cs-text", next);
      return;
    }

    var contrastButton = event.target.closest("[data-toggle-contrast]");
    if (contrastButton) {
      var mode = root.getAttribute("data-contrast") === "high" ? "normal" : "high";
      applyContrast(mode);
      write("cs-contrast", mode);
      return;
    }

    var audioButton = event.target.closest("[data-toggle-audio]");
    if (audioButton) {
      var state = audioButton.getAttribute("aria-pressed") === "true" ? "off" : "on";
      applyAudio(state);
      write("cs-audio", state);
    }
  });
})();
