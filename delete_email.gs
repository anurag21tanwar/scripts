/* google app script to create a label and add email threads to label and delete those emails. */

function _getNaggingLabel() {
  var nagging_label_text = "delete me";
  var label = GmailApp.getUserLabelByName(nagging_label_text);
  if (label == null) {
    var label = GmailApp.createLabel(nagging_label_text);
  }
  return label;
}

function addNaggingLabels() {
  var label = _getNaggingLabel();
  var threads = GmailApp.search('older_than:3d');
  for (var i = 0; i < threads.length; i++) {
    label.addToThread(threads[i]);
  }
}

function cleanUp() {
  var delayDays = 3
 
  var maxDate = new Date();
  maxDate.setDate(maxDate.getDate()-delayDays);
 
  var label = GmailApp.getUserLabelByName("delete me");
  var threads = label.getThreads();
  for (var i = 0; i < threads.length; i++) {
    if (threads[i].getLastMessageDate()<maxDate)
    {
      threads[i].moveToTrash();
    }
  }
}
