// File#: _2_multiple-custom-select-v2
// Usage: codyhouse.co/license
(function() {
    var MultiCustomSelectTwo = function(element) {
      this.element = element;
      this.checkboxes = this.element.getElementsByClassName('js-multi-select-v2__input');
      this.counter = this.element.getElementsByClassName('js-multi-select-v2__selected-items-counter');
      this.resetBtn = this.element.getElementsByClassName('js-multi-select-v2__reset');
      this.checkedClass = 'multi-select-v2__label--checked';
      initMultiCustomSelectTwo(this);
    };
  
    function initMultiCustomSelectTwo(element) {
      // init number of checked inputs
      resetCounter(element);
      // init checked classes
      initCheckedClass(element);
  
      // detect input checked/unchecked
      element.element.addEventListener('change', function(event){
        var label = event.target.closest('label');
        if(label) Util.toggleClass(label, element.checkedClass, event.target.checked);
        resetCounter(element);
      });
  
      // reset checked inputs
      if(element.resetBtn.length > 0) {
        element.resetBtn[0].addEventListener('click', function(event) {
          for(var i = 0; i < element.checkboxes.length; i++) element.checkboxes[i].checked = false;
          resetCounter(element, 0);
          resetCheckedClasses(element);
        });
      }
    };
  
    function resetCounter(element, value) {
      // update number of selected checkboxes
      if(element.counter.length < 1) return;
      if(value !== undefined) {
        element.counter[0].textContent = value;
        return;
      }
  
      var count = 0;
      for(var i = 0; i < element.checkboxes.length; i++) {
        if(element.checkboxes[i].checked) count = count + 1;
      }
      element.counter[0].textContent = count;
    };
  
    function resetCheckedClasses(element) {
      var checkedLabels = element.element.getElementsByClassName(element.checkedClass);
      while(checkedLabels[0]) {
        Util.removeClass(checkedLabels[0], element.checkedClass);
      }
    };
  
    function initCheckedClass(element) {
      for(var i = 0; i < element.checkboxes.length; i++) {
        if(element.checkboxes[i].checked) {
          var label = element.checkboxes[i].closest('label');
          if(label) Util.addClass(label, element.checkedClass);
        }
      }
    };
  
    //initialize the CustomSelect objects
      var customSelect = document.getElementsByClassName('js-multi-select-v2');
      if( customSelect.length > 0 ) {
          for( var i = 0; i < customSelect.length; i++) {
              (function(i){new MultiCustomSelectTwo(customSelect[i]);})(i);
          }
    }
  }());