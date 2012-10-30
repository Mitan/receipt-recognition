package com.example;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;


public class AddTrans extends Activity{
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.transaction);
        TextView tv=(TextView) findViewById(R.id.name_card);
        tv.clearComposingText();
        tv.setText(getIntent().getStringExtra("name_card").toString());
    }
}
