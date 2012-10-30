package com.example;

import android.app.Activity;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup.LayoutParams;
import android.widget.*;

import java.util.ArrayList;


public class MyActivity extends Activity {

    private ArrayList<String> card=new ArrayList<String>();
    private ArrayAdapter<String> adapter;
                               private static final int ADD_CARD_ACTIVITY = 9;
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        card.add("Card №1");
        card.add("Card №2");
        card.add("Card №3");
        ListView lvMain = (ListView) findViewById(R.id.lvMain);
        adapter = new ArrayAdapter<String>(this,
                android.R.layout.simple_list_item_1, card);
        lvMain.setAdapter(adapter);
        Button addButton=(Button)findViewById(R.id.add_card);
        View.OnClickListener onClickListener=new View.OnClickListener(){
            public void onClick(View view){
                switch (view.getId()){
                    case R.id.add_card:
                        Intent intent = new Intent(MyActivity.this,AddCardActivity.class);
                        startActivityForResult(intent,ADD_CARD_ACTIVITY);
                }
            }
        };
       addButton.setOnClickListener(onClickListener);
        lvMain.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                String item=card.get(i);
                Intent intent = new Intent(MyActivity.this,AddTrans.class);
                intent.putExtra("name_card",card.get(i));
                startActivity(intent);
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == ADD_CARD_ACTIVITY) {
            String name = data.getStringExtra("FirstName");
            String family=data.getStringExtra("LastName");
            card.add(name+" "+family);
            adapter.notifyDataSetChanged();
        }
    }

}