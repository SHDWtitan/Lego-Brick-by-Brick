// onload scripts
document.getElementById("defaultOpen").click()
AOS.init(); // activating the scrolling library


function popularityOpen(event, popup) {
    console.log("hello")
    var panel = document.getElementById(popup);
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
      panel.style.opacity = "0%";
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
      panel.style.opacity = "100%";
    }
}

function openGraph(evt, song) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(song).style.display = "block";
    evt.currentTarget.className += " active";
  }