#!/bin/sh
echo '<?xml version="1.0" encoding="UTF-8"?>'
echo '<patches>'
for f in $*; do
  n=${f//httpd-[0-9.]*-/}
  n=${n//.patch/}
  s_HEAD=`grep ^Upstream-HEAD $f | sed 's/Upstream-HEAD: //'`
  s_20=`grep ^Upstream-2.0: $f | sed 's/Upstream-2.0: //'`
  s_Com=`grep ^Upstream-Status: $f | sed 's/Upstream-Status: //'`
  printf '<patch name="%s" status-head="%s" status-2.0="%s" status-comment="%s"/>\n' \
      $n "$s_HEAD" "$s_20" "$s_Com"
done
echo '</patches>'
