$('.get-more').live("click", function() {
    var contents = $(this).parent().children('.more-contents');
    contents.toggleClass('hidden');
    return false;
});

$('.first-claim').live("click", function() {
    // if not a single-claimant task
    if (!($(this).hasClass('single-claimant'))) {
        // add 'claimed by' section
        stuff = '<div class="claimed-by"><h5>Claimed by <span class="claimant-number">1</span> person:</h5><div class="claimants"><img src=""></div></div>';
        $(this).parent().prepend(stuff);
    }
    else {
        $(this).addClass('single-claimed');
    }
    $(this).removeClass('first-claim');
    $(this).addClass('claimed');
    $(this).text('Claimed');
    return false;
});

$('.addl-claim').live("click", function() {
    numClaimants = parseInt($(this).parent().find('span').text());
    numClaimants = numClaimants + 1;
    $(this).parent().find('span').text(numClaimants + "");
    $(this).removeClass('addl-claim');
    $(this).addClass('claimed');
    $(this).text('Claimed');
    return false;
});